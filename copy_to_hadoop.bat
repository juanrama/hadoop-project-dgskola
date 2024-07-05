@echo off
setlocal

REM Define local and destination paths
set "local_path=E:\Projek\hadoop-project"
set "docker_container_name=hadoop-project-namenode-1"
set "docker_destination=/hadoop-project"
set "hadoop_destination=/dgskola"

REM Step 1: Move files to Docker container
for %%f in (%local_path%\result_*.csv) do (
    echo Copying %%f to Docker container...
    docker cp "%%f" "%docker_container_name%:%docker_destination%"
)

REM Step 2: Run Hadoop commands in the Docker container
echo Running Hadoop copy commands in the Docker container...
docker exec -it %docker_container_name% bash -c "hadoop fs -copyFromLocal %docker_destination%/* %hadoop_destination%"

echo All files have been copied to Hadoop.

endlocal
pause