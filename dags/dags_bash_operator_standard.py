import datetime
import pendulum
from airflow import DAG
from airflow.operator.bash import BashOperator

my_dag=DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 9 * * 1,5",
    start_date=pendulum.datetime(2024,6,1, tz="Asia/Seoul"),
    tag="homework",
)

BashOperator(task_id="bash_t1", 
             bash_command="whoami", 
             dag=my_dag)
BashOperator(task_id="bash_t2", 
             bash_command="echo $HOSTNAME",
             dag=my_dag)

