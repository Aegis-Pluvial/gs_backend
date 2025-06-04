def test_read_root(client):
    # "Deve retornar OK e Hello World!"

    response = client.get('/api')  # Act (ação)

    assert response.status_code == 200  # Assert (Afirmação)

    assert response.json() == {'message': 'api root'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"
