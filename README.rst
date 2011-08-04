================
codespeed-client
================

Library and command-line tool to push benchmark data to CodeSpeed.

Usage as library: ::

    from codespeed_client import Client
    client = Client('http://codespeed.example.net', environment='Test Environment', project='Project')
    client.add_result(commitid=1278, benchmark='primes', result_value=42.0)
    client.add_result(commitid=1278, benchmark='ai',     result_value=7)
    client.upload_results()

As command-line tool: ::

    codespeed-client --environment='Test Environment' --project=Project --commitid=1278 --benchmark=primes --result-value=42.0
    codespeed-client --environment='Test Environment' --project=Project --commitid=1278 --benchmark=ai     --result-value=7
