================
codespeed-client
================

Library and command-line tool to push benchmark data to CodeSpeed.

Tested with Python 2.6, 2.7 and 3.2. Versions < 2.6 will not work, 3.x may work but not tested.

Usage as library: ::

    from codespeed_client import Client

    # kwargs list: environment, project, benchmark, branch, commitid, revision_date, executable,
    #              result_date, result_value, max, min, std_dev

    # kwargs passed to constructor are defaults
    client = Client('http://codespeed.example.net', environment='Test Environment', project='Project')

    # kwargs passed to add_result overwrite defaults
    client.add_result(commitid=1278, benchmark='primes', result_value=42.0)
    client.add_result(commitid=1278, benchmark='ai',     result_value=7)

    # upload all results in one request
    client.upload_results()

As command-line tool: ::

    codespeed-client --help
    codespeed-client --environment='Test Environment' --project=Project --commitid=1278 \
                     --benchmark=primes --result-value=42.0
    codespeed-client --environment='Test Environment' --project=Project --commitid=1278 \
                     --benchmark=ai --result-value=7
