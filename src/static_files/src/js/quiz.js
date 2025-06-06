const botao = document.getElementById("botao-enviar");
const resFinal = document.getElementById("resultado");
const gabarito = ['c', 'b', 'b', 'c', 'b', 'c', 'b', 'b', 'b', 'b'];

function obterResposta(numQuestao) {
    const seletor = `input[name="p${numQuestao}"]:checked`;
    const inputSelecionado = document.querySelector(seletor);

    if (inputSelecionado) {
        return inputSelecionado.value;
    }
    return null;
}

botao.addEventListener("click", () => {
    let acertos = 0;
    const respostasUsuario = [];

    for (let i = 1; i <= 10; i++) {
        const resposta = obterResposta(i); 

        respostasUsuario.push(resposta);
    }
    for (let i = 0; i < gabarito.length; i++) {
        if (respostasUsuario[i] === gabarito[i]) {
            acertos++; 
        }
    }
    resFinal.textContent = `Você acertou ${acertos}/10. ou ${(acertos/10) * 100}% das questões`;
});