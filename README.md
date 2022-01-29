# CI pipeline for simple FastAPI server

### VAGRANT
```
vagrant destroy -f && vagrant up
vagrant status
```

### GITLAB 
```bash
curl -d '{"url": "https://testurl.com/"}' -H "Content-Type: application/json" -X POST  http://127.0.0.1:8003/shorten
```

To manually push in registry:
```bash
docker login gitlab2.atp-fivt.org:5050

docker build -t gitlab2.atp-fivt.org:5050/tpos2021/podkidysheval-practice .

docker push gitlab2.atp-fivt.org:5050/tpos2021/podkidysheval-practice
```

docker-compose run

```bash
docker-compose up --build && docker-compose rm -fs
 ```

*`config.toml` – file with gitlab docker executor

### More Project CI full circle project with ansible
1. https://www.bevuta.com/en/blog/continuous-delivery-with-gitlab-ci-and-ansible-part-2/
2. https://github.com/vyuldashev/ansible-role-gitlab-pipeline-artifacts/blob/master/tasks/main.yml
3. https://blog.callr.tech/gitlab-ansible-docker-ci-cd/
4. https://blog.callr.tech/gitlab-ansible-docker-swarm-ci-cd/
5. https://medium.com/geekculture/how-to-run-an-ansible-playbook-using-gitlab-ci-cd-2135f76d7f1e
6. https://devopsquare.com/a-complete-overview-of-ansible-264bb0cceafe
7. Ansible with flask https://github.com/brennv/flask-ansible-example
