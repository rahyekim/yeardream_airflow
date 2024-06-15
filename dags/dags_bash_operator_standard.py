import datetime
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

my_dag=DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 9 * * 1,5",
    start_date=pendulum.datetime(2024,6,1, tz="Asia/Seoul"),
    tags=["homework"],
    catchup=False,
)

bash_t1=BashOperator(task_id="bash_t1", 
             bash_command="echo whoami", 
             dag=my_dag)
bash_t2=BashOperator(task_id="bash_t2", 
             bash_command="echo $HOSTNAME",
             dag=my_dag)

bash_t1 >> bash_t2