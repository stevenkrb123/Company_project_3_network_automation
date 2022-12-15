import asyncio
import asyncssh
import getpass


async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)


# this coroutine will take a list of hosts and call or await the run_client() coroutine for each host.
async def run_multiple_clients(hosts):  #in previous asyncio examples the name of the top-level coroutine was main,
                                        # but this is not mandatory

    tasks = list()
    for host in hosts:

        task =  run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True) # I want it to raise an Exception if it's the case.


    i = 0
    for result in results:
        i += 1

        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')

        elif result.exit_status != 0:
            print(f'Task {i} exited with status {result.exit_status}:')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')

        print(50 * '#')

password = getpass.getpass('Enter Password:')
hosts = [
    {'host': '10.1.1.10', 'username': 'khoadang', 'password': password, 'command': 'enable'},
    {'host': '10.1.1.20', 'username': 'khoadang', 'password': password, 'command': 'enable'},
    {'host': '10.1.1.30', 'username': 'khoadang', 'password': password, 'command': 'enable'}
]

asyncio.run(run_multiple_clients(hosts))