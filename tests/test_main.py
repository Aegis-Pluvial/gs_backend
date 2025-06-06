def test_read_root(client):  # Utiliza da fixture feita em conftest para chamar o client-side da aplicação
    # "Deve retornar OK e Hello World!"

    response = client.get('/api')  # Act (ação)

    assert response.status_code == 200  # Assert (Afirmação)

    assert response.json() == {'message': 'api root'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"
