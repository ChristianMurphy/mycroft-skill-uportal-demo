## uPortal Demo Skill

> A demo of capabilities for voice control of uportal

## Examples

* "What's due today?"
* "What's for lunch?"
* "What classes do I have today?"

## Try it out with Docker

```sh
docker pull mycroftai/docker-mycroft

docker run -d \
-v directory_on_local_machine:/root/.mycroft \
--device /dev/snd \
-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
-v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
-p 8181:8181 \
--name mycroft mycroftai/docker-mycroft

docker exec -it mycroft /opt/mycroft/msm/msm install https://github.com/ChristianMurphy/mycroft-skill-uportal-demo
```
