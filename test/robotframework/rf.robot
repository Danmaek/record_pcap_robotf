*** Settings ***
Library     Process
Library     lib/sn.py


*** Test Cases ***
Test curl fonctionnality
    ${ret}    sn.Start    "100"
    Log    ${ret}
    ${websiteData}    Run Process    curl http://localhost:8000    shell=True
    ${ret}    sn.stop
    Log    ${ret}
    Log    ${websiteData.stdout}
    Should Contain    ${websiteData.stdout}    <h1>Welcome in my server</h1>
