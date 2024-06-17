from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg2",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2024,5,1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # start_date= 2주전 월요일 / end_date=2주전 토요일 (YYYY-MM-DD)
    bash_task_2= BashOperator(
        task_id= 'bash_task_2',
        env={'START_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19)) }}',
             'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") -macros.dateutil.relativedelta.relativedelta(days=14) | ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )
    
    bash_task_3= BashOperator(
        task_id= 'bash_task_3',
        env={'START_DATE':'{{ (data_interval_start.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=5)) }}',
             'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") -macros.dateutil.relativedelta.relativedelta(weeks=2) | ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )
        
    
    bash_task_2 >> bash_task_3