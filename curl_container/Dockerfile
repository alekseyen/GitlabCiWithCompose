FROM curlimages/curl:7.80.0

USER root

COPY curls_command.sh /

RUN chmod +x /curls_command.sh

ENTRYPOINT ["./bin/sh"]

CMD ["/curls_command.sh"]
