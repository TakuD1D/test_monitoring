import subprocess

# test docker containe stats

def test_docker_stats():
    cmd = 'docker container stats'
    try:
        process = subprocess.run(cmd.split(), stdout=subprocess.PIPE, timeout=5,encoding='utf-8')
        print(process)
    except subprocess.TimeoutExpired as e:
        print('Timeout')
        print(e.output)
    # output, error = process.communicate()
    # print(output.decode('utf-8'))
    # print(process.stdout)
    
if __name__ == '__main__':
    test_docker_stats()