helm dep build

helm install --name lukeaddison-blog --namespace lukeaddison .

helm upgrade lukeaddison-blog .

helm del --purge lukeaddison-blog