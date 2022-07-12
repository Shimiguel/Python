# Aula #08 - Módulos
 * canal [Curso em Vídeo](https://www.youtube.com/c/CursoemV%C3%ADdeo)
 * [Curso de Python #08 - Utilizando Módulos](https://www.youtube.com/watch?v=oOUyhGNib2Q&t=358s)
 ## Índice
  * [O que são](#o-que-são)
  * [Como importar](#como-importar)

 ## O que são
  São como ferramentas de fora do Python, que precisarão ser *importadas* para dentro dele. E só assim podem ser utilizadas, elas permitem executar códigos de forma mais fácil e até em aguns casos, executar comandos e tarefas que não consiguiríamos somente com o Python.

 ## Como importar
  Como explicado na aula lá no canal do Curso em vídeo, podemos importar-los de 2 maneiras, pelo `import nome_módulo` ou `from nome_módulo import nome_ferramenta`, o primeiro serve para importarmos todo o módulo, o segundo a "ferramenta" específica dentro do módulo.
  ```python
  import estou_sem_criatividade 
  #importou todo o módulo de nome "estou_sem_criatividade"
  ```
  ```python
  from estou_sem_criatividade import exemplo
  #importou a ferramenta de nome "exemplo", do módulo de nome "estou_sem_criatividade".
  ```
