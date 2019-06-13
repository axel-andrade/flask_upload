%{
 1 - Dada a matriz [2 10 7 6; 3 12 25 9]
%}

%a) Acrescente uma terceira linha a matriz com os elementos 30 21 19 1

mat = [2 10 7 6; 3 12 25 9];
mat =[mat; [30 21 19 1]]; 

%(b) Defina uma matriz B que contenha as três primeiras linhas da matriz A e as
% colunas de 2 a 5

matB = mat(1:3,2:2:4);

%2 - Criar um vetor com componente ímpares entre 31 e 75

array = (31:2:75);

%3 - Seja x = [3 2 6 8]’ e y = [4 1 3 5]’ (vetores colunas)
%a) Somar x e y: 

x = [3;2;6;8];
y = [4;1;3;5];
sumXY = x+y;
pot = (x.^y);

% 4 - Crie um vetor x com componentes
n = (1:100);
x = -1 * n + 1./(2*n +1);
y = sum(x);

% 5 - Crie um vetor com o comando randi(100,1,10). Encontre qual é o maior valor neste
% vetor e seu índice. Substitua pelo seu quadrado. Dica: verifique o funcionamento da
% função max

random = randi(100,1,10);
maxValue = max(random);
minValue = min(random);

% 6 - Considere a matriz M = [10 2 10 5; 2 5 1 6; 2 4 8 10;4 10 3 5]. Substitua os valores
% da primeira coluna e da última linha por 1. Utilize o comando find para encontrar
% na terceira linha desta matriz os índices dos valores maiores que 5. Troque estes
% valores por 5.

M = [10 2 10 5; 2 5 1 6; 2 4 8 10;4 10 3 5];
M(:,1) = 1;
M(4,:) = 1;
ind = find(M(3,:) > 5);

% 7 - 

n = 255;
k = (1:n);
x = 1./k;
y = sum(x);

% 8 

ant = 4;
row1 = (1:7);
row2 = (9:-2:-3);
row3 = (ant:ant:28);
matR = [row1;row2;row3];

%10

x = logspace(-2,-1,500);
y = sin(1./x);
plot(x,y);





