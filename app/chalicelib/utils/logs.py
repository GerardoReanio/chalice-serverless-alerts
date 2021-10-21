import boto3
from datetime import datetime, timedelta
import time

def get_data_cw(fini, ffin, region_name, query, log_group ):

    session = boto3.Session(region_name=region_name)
    client = session.client('logs')

    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=fini, 
        endTime=ffin, # hoy
        queryString=query,
        limit=1000
    )

    query_id = start_query_response['queryId']
    response = None

    while response == None or response['status'] == 'Running':
        print('Waiting for query to complete ...')
        time.sleep(1)
        response = client.get_query_results(
            queryId=query_id
        )

    print("Total de datos obtenidos: {}".format(len(response['results'])))
    return response


def clean_data_response(response):
    try:
        rptval = response['results'][0]
        labels = list()
        for i in rptval:
            labels.append((list(i.values())[0]))

        for l in labels:
            exec("{} = list()".format(l))

        for i, rpt in enumerate(response['results']):
            if len(rpt) == len(labels):
                for j, l in enumerate(labels):
                    if l in list(rpt[j].values()):
                        eval(l).append(list(rpt[j].values())[1])
            else:
                print("[EXCLUDE] Datos Incompletos:{}".format(rpt))
                
        frames = list()
        for lb in labels:
            frames.append(eval(lb))
        return frames
    
    except Exception as e:
        print(e)
        print('No Data')
        

def get_response_time_merchantAvg(val_minute):
    ffin = int(datetime.now().timestamp() *1000)
    fini = int((datetime.now() - timedelta(minutes=val_minute)).timestamp() * 1000)
    
    query = 'fields @timestamp, @message \
        | stats avg(properties.elapsed) as ResponseTimeMerchantAvg , \
            count(properties.elapsed) as TotalNotificationsAnalized \
        | filter properties.Application like "ApiNotificationService" \
        | filter message Like "Notificación aceptada por la URL" \
        | filter properties.result.IsSuccessStatusCode = 1 \
        | sort ResponseTimeMerchantAvg desc'

    region_name = 'us-east-1'

    log_group = 'microservice-notificaciones'

    response = get_data_cw(fini, ffin, region_name, query, log_group )
    ResponseTimeMerchantAvg = clean_data_response(response)
    
    return (float(ResponseTimeMerchantAvg[0][0]), int(ResponseTimeMerchantAvg[1][0]))