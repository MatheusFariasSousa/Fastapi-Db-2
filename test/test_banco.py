
from fastapi import status

def test_health_check(client):
    response = client.get("/index")
    print(response.json())

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Health-Check"

def test_get_all(client):
    response = client.get("/sql/get_all")
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {"Users":[{"id":1,"nome":"Matheus","cpf":"12345678910"}]}

def test_post(client):
    user = {"nome":"Carlos",
            "cpf":"99999999999"}
    response = client.post("/sql/post",json=user)


    assert response.status_code == status.HTTP_201_CREATED

    assert response.json() =={"id":2,"nome":"Carlos",
            "cpf":"99999999999"}
    
def test_delete(client):
    response = client.delete(f"/sql/delete/{1}")
    assert response.status_code == status.HTTP_200_OK

    assert response.json()=={"id":1,"nome":"Matheus","cpf":"12345678910"}

def test_update(client):
    user = {"nome":"Carlos",
            "cpf":"99999999999"}
    response = client.put(f"/sql/put/{1}",json=user)
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {"id":1,"nome":"Carlos",
            "cpf":"99999999999"}




    






    





    

    


    



        































    
#def test_delete(client):
#
#    teste=client.post("/Dicionario/post/Matheus")
#    dicionario = teste.json()    
#    response = client.delete(f'/Dicionario/delete/1')
 
    
#    assert response.json() == dicionario   
        
    

    

    
    

