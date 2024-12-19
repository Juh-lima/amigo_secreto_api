## Sobre o projeto
    *Uma API desenvolvida para simplificar a organização do tradicional evento "amigo oculto", 
    utilizando os conceitos de arquitetura limpa(Clean Architecture) e escrita em Python.
    *Optei por utilizar o Litestar e o SQLAlchemy(ORM).

## Principais funcionalidades   
   
    *Registro de participantes do evento.
    *Sorteio automatizado para definir os pares do amigo oculto.
    *Exibição dos pares gerados no sorteio.
    *Personalização de regras opcionais, como a exclusão de determinados pares.

## Explanação de entidades
    * O sistema foi concebido com quatro entidades que julgo fundamentais:

        *Usuário: Gerencia informações pessoais e dados de autenticação.
        *Participação: Representa o vínculo de um usuário com um evento específico.
        *Evento: Define a realização de um amigo oculto, associado a um líder que é um Participante.
        *Presente: Representa os itens da lista de desejos de um Participante.

## Objetivo 

    *Facilita a criação e o registro de sorteios de amigo oculto, oferecendo uma solução prática para organizar a brincadeira entre amigos.

## Limitações 

    *O aplicativo não rastreia o envio de presentes ou identifica quem presenteou quem. Seu foco é exclusivamente simplificar o processo de sorteio.