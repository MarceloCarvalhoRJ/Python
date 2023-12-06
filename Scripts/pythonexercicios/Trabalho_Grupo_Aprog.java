public import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class APROG_LEI_DA_1231893_1230595 {
    static final String FILE_CIDADES = "cidades.txt";
    static final int NR_CIDADES = 7;
    static final String FILE_DISTANCIAS = "distancias_entre_cidades_2.txt";
    /*** 1º - Verificar a qtde de cidades do arquivo novo e mudar o vlr na constante NR_CIDADES. ***
     *** 2º - Incluir o nome da cidade no arquivo cidades.txt. ***/
    static final String FILE_PLANEAMENTO = "planeamento.txt";

    public static void main(String[] args) throws FileNotFoundException {

        // Cria array cidades com alvará.
        String[] cidades = criaArrayCidades(FILE_CIDADES);

        // Cria a matriz das distâncias entre as cidades.
        int[][] distanciasEntreCidades = arrayDistanciasEntreCidades(FILE_DISTANCIAS);

        // Cria matriz para guardar o AutoCarro mais próximo e um determinado dia. (J)
        int[][] autoCarroMaisProximo = new int[1][2];

        // A) Faz a leitura do arquivo txt e cria a matriz do planeamento.
        int[][] planeamento = lerPlaneamento(FILE_PLANEAMENTO, autoCarroMaisProximo);
        lerPlaneamento(FILE_PLANEAMENTO, autoCarroMaisProximo);

        // B) Visualiza a matriz do planeamento.
        showArrayPlanemento(planeamento);

        // C) Cria e visualiza a matriz de kilometragem de cada autocarro por dia.
        int[][] kmAutocarrosPorDia = criakmAPercorrerCadaAutocarro(distanciasEntreCidades, planeamento);
        showKmAPercorrerPorCadaAutoCarro(kmAutocarrosPorDia, planeamento);

        // D) Cria e visualiza a matriz de kilometragem por Autocarro.
        int[] totalKmPorCarro = calcularTotalKmPorAutocarro(kmAutocarrosPorDia);
        showTotalKmPorAutoCarro(totalKmPorCarro);

        // E) Cria e visualiza a kilometragem total dos Autocarros.
        showTotalKmDaFrota(retornaTotalKmFrota(totalKmPorCarro));

        // F) Calcula e visualiza o maximo de km percorridos pela frota em um dia.
        visualizarMaxKmDiarioFrota(kmAutocarrosPorDia);

        // G) Visualiza autocarros que permanecem mais de 1 dia consecutivo na mesma cidade.
        showAutocarrosParados(planeamento);

        // H) Visualizar o dia mais tardio e a cidade, em que todos os autocarros estarão na mesma cidade;
        showAutocarroTardioNaMesmaCidade(cidades, planeamento);

        // I) calcula e visualiza o percentual/histograma dos autocarros.
        showHistogramaDasPorcentagens(calcularPorcentagemKmAutoCarros(totalKmPorCarro, retornaTotalKmFrota(totalKmPorCarro)));

        // J) Visualiza o Autocarro mais proximo.
        //*** Alterar o output para mais de um carro.
        visualizaAutocarroMaisProximo(cidades, autoCarroMaisProximo, planeamento, distanciasEntreCidades);

        System.out.println();
        System.out.println(Arrays.toString(criaArrayCidades(FILE_CIDADES)));

    }


    private static int[][] lerPlaneamento(String filePlaneammento, int[][] autoCarroMaisProximo) throws FileNotFoundException {
        Scanner in = new Scanner(new File(filePlaneammento));
        // Ignora a primeira linha.
        in.nextLine();
        // Lê os elementos da 2.ª linha do arquivo planeamento "3 6" que representam o tamanho da array a ser criada.
        int linhas = in.nextInt();
        int colunas = in.nextInt();
        // Cria a matriz do planeamento.
        int[][] planeamento = new int[linhas][colunas];
        //‘Loop’ para preencher a matriz com restante das informações.
        for (int l = 0; l < linhas; l++) {
            for (int c = 0; c < colunas; c++) {
                planeamento[l][c] = in.nextInt();
            }
        }
        autoCarroMaisProximo[0][0] = in.nextInt();
        autoCarroMaisProximo[0][1] = in.nextInt();
        in.close();
        return planeamento;
    }

    private static void showArrayPlanemento(int[][] planeamento) {
        gerarLinhaDivisoria('-', 31, "B");
        for (int x = 0; x < planeamento.length; x++) {
            System.out.printf("Bus%d :", x);
            for (int y = 0; y < planeamento[0].length; y++) {
                System.out.printf("%4d", planeamento[x][y]);
            }
            System.out.println();
        }
    }

    private static int[][] criakmAPercorrerCadaAutocarro(int[][] distanciasEntreCidades, int[][] planeamento) {
        /* cria uma array com o mesmo tamanho da array planeamento para guardar
           a km por dia a percorrer por cada autocarro. */
        int[][] kmAutocarrosPorDia = new int[planeamento.length][planeamento[0].length];

        // ‘Loop’ para o preenchimento da array utilizando a km correspondente da array distanciasEntreCidades.
        for (int l = 0; l < kmAutocarrosPorDia.length; l++) {
            //preencher com zeros todas as linhas da coluna 0.
            kmAutocarrosPorDia[l][0] = 0;
            //loop para preenchimento das colunas.
            for (int c = 1; c < kmAutocarrosPorDia[0].length; c++) {
               /* utilizamos o valor da linha e coluna da posicao atual e anterior da array planemento
                  como coordenadas das posicoes cidadeOrigem (linha) e cidadeDestino (coluna) para acessar
                  o valor correspondente na array distanciasEntreCidades. */
                int cidadeOrigem = planeamento[l][c - 1];
                int cidadeDestino = planeamento[l][c];
                kmAutocarrosPorDia[l][c] = distanciasEntreCidades[cidadeOrigem][cidadeDestino];
            }
        }
        return kmAutocarrosPorDia;
    }

    private static void showKmAPercorrerPorCadaAutoCarro(int[][] kmAutocarrosPorDia, int[][] planeamento) {
        gerarLinhaDivisoria('-', 31, "C");
        //System.out.println(" // Km a percorrer por cada autocarro.");
        for (int x = 0; x < planeamento.length; x++) {
            System.out.printf("Bus%d :", x);
            for (int y = 0; y < planeamento[0].length; y++) {
                System.out.printf("%4d", kmAutocarrosPorDia[x][y]);
            }
            System.out.println();
        }
    }

    private static int[] calcularTotalKmPorAutocarro(int[][] kmAutocarrosPorDia) {
        int[] totalKmPorCarro = new int[kmAutocarrosPorDia.length];
        int somaKm;
        for (int l = 0; l < kmAutocarrosPorDia.length; l++) {
            somaKm = 0;
            for (int c = 0; c < kmAutocarrosPorDia[0].length; c++) {
                somaKm += kmAutocarrosPorDia[l][c];
            }
            totalKmPorCarro[l] = somaKm;
        }
        return totalKmPorCarro;
    }

    private static void showTotalKmPorAutoCarro(int[] totalKmPorCarro) {
        gerarLinhaDivisoria('-', 31, "D");
        //System.out.println(" // Total de Km por Autocarro.");
        for (int l = 0; l < totalKmPorCarro.length; l++) {
            System.out.printf("Bus%d : %d Km%n", l, totalKmPorCarro[l]);
        }
    }

    private static int retornaTotalKmFrota(int[] totalKmPorCarro) {
        int totalKmFrota = 0;
        for (int l = 0; l < totalKmPorCarro.length; l++) {
            totalKmFrota += totalKmPorCarro[l];
        }
        return totalKmFrota;
    }

    private static void showTotalKmDaFrota(int totalKmFrota) {
        gerarLinhaDivisoria('-', 45, "E");
        System.out.printf("Total de km a percorrer pela frota = %d km%n", totalKmFrota);
    }

    private static void visualizarMaxKmDiarioFrota(int[][] kmAutocarrosPorDia) {
        int qtdeAutocarros = kmAutocarrosPorDia.length;
        int qtdeDias = kmAutocarrosPorDia[0].length;
        int somaKmDia = 0;
        int maxKmDiario = 0;
        // criando uma array para armazenar o total de km por dia, pois vamos precisar para verificar se há dias com essa mesma km.
        int[] totalKmDiario = new int[qtdeDias];
        // ‘Loop’ invertido, pois vamos percorrer primeiro todas as linhas de cada coluna.
        for (int c = 0; c < qtdeDias; c++) {
            for (int l = 0; l < qtdeAutocarros; l++) {
                somaKmDia += kmAutocarrosPorDia[l][c];
            }
            //preenchimento da array com o total de km dia.
            totalKmDiario[c] = somaKmDia;
            if (somaKmDia > maxKmDiario) {
                maxKmDiario = somaKmDia;
            }
            // resetando a soma para o próximo dia.
            somaKmDia = 0;
        }
        gerarLinhaDivisoria('-', 45, "F");
        //System.out.println(" // máximo de kms num dia.");
        System.out.printf("máximo de kms num dia: (%d km), dias: ", maxKmDiario);
        // Percorrendo a array para poder imprimeír os dias com a mesma km.
        for (int dia = 0; dia < qtdeDias; dia++) {
            if (maxKmDiario == totalKmDiario[dia]) {
                System.out.printf("[%d]", dia);
            }
        }
        System.out.println();
    }

    private static void showAutocarrosParados(int[][] planeamento) {
        gerarLinhaDivisoria('-', 83, "G");
        System.out.print("Autocarros que permanecem mais de 1 dia consecutivo na mesma cidade: ");
        boolean naoHaAutocarro = true;
        for (int l = 0; l < planeamento.length; l++) {
            /* Flag para evitar que imprima mais de uma vez o mesmo autocarro, caso permaneça
               na mesma cidade mais de 2 dias consecutivos.*/
            boolean diasConsecutivos = false;
            // Reseta a variavel para cada mudança de autocarro(linha).
            //‘Loop’ que verifica se todos os elementos da coluna são iguais. ***
            for (int c = 1; c < planeamento[0].length; c++) {
                if (planeamento[l][c - 1] == planeamento[l][c] && !diasConsecutivos) {
                    System.out.printf("Bus%d ", l);
                    diasConsecutivos = true;
                    naoHaAutocarro = false;
                }
            }
        }
        // Mensagem caso não haja autocarro. É preciso, senão fica em branco e pode causar confusão.
        if (naoHaAutocarro) {
            System.out.print("Não há autocarros para esse planeamento.");
        }
        System.out.println();
    }

    private static void showAutocarroTardioNaMesmaCidade(String[] cidades, int[][] planeamento) {
        /* Inicializa com -1, pois = 0 pode coincidir com o "dia 0" se por acaso todos
           os autocarros estiverem na mesma cidade no primeiro dia e assim monstra esse dia.
           Obs. Antes na linha 103 estava: (diaMaisTardio != 0). */
        int diaMaistardio = -1;
        int cidade = 0;
        for (int dia = 0; dia < planeamento[0].length; dia++) {
            // reseta as variaveis a cada mudança de dia.
            int linha = 1;
            boolean busMesmaCidade = true;
            // Encerra o ‘loop’ pelo total das linhas ou se alguma cidade nao for igual.
            while (linha < planeamento.length && busMesmaCidade) {
                if (planeamento[linha - 1][dia] != planeamento[linha][dia]) {
                    busMesmaCidade = false;
                }
                linha++;
            }
            if (busMesmaCidade) {
                // dia mais tardio representa a coluna do Array Planeamento.
                diaMaistardio = dia;
                // cidade recebe o elemento do Array Planeamento que se refere ao número da cidade.
                cidade = planeamento[linha - 1][dia];
            }
        }
        gerarLinhaDivisoria('-', 51, "H");
        //System.out.println(" // Autocarros na mesma cidade no dia mais tardio.");
        if (diaMaistardio != -1) {
            System.out.printf("No dia <%d>, todos os autocarros estarão em <%s>%n", diaMaistardio, obterNomeCidade(cidades, cidade));
        } else {
            System.out.println("Nenhum autocarro encontrado no planeamento.");
        }
    }

    private static String[] criaArrayCidades(String fileCidades) throws FileNotFoundException {
        // Abre o ficheiro contendo as cidades.
        Scanner in = new Scanner(new File(fileCidades));
        //Cria e salva na array todas as cidades da linha separadas por "," .
        String[] cidades = in.nextLine().split(",");
        in.close();
        return cidades;
    }

    private static String obterNomeCidade(String[] cidades, int numeroCidade) {
        return cidades[numeroCidade];
    }

    private static void showHistogramaDasPorcentagens(double[] calcularMediaAutoCarros) {
        gerarLinhaDivisoria('-', 23, "I");
        for (int l = 0; l < calcularMediaAutoCarros.length; l++) {
            System.out.printf("bus%d (%.2f%%) :", l, calcularMediaAutoCarros[l]);
            //Imprimi cada asteristico que representa 10 pontos percentuais.
            for (int a = 1; a <= calcularMediaAutoCarros[l] / 10; a++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    // verificar array totalkmfrota precisa apenas variavel
    // Totalkmcarro deve ser uma array unidimensional
    //re
    private static double[] calcularPorcentagemKmAutoCarros(int[] totalKmPorCarro, int totalKmFrota) {
        int qtdeAutocarros = totalKmPorCarro.length;
        double[] percentualKmPorBus = new double[qtdeAutocarros];
        for (int l = 0; l < totalKmPorCarro.length; l++) {
            for (int c = 0; c < totalKmPorCarro.length; c++) {
                percentualKmPorBus[l] = ((double) totalKmPorCarro[l] / totalKmFrota) * 100;
            }
        }
        return percentualKmPorBus;
    }

    private static void visualizaAutocarroMaisProximo(String[] cidades, int[][] autoCarroMaisProximo, int[][] planeamento, int[][] distanciasEntreCidades) {
        //ATENCÂO!!! Quando coincidir de todos os autocarros estarem na mesma cidade no mesmo dia, qual o critério de escolha do ??? ***
        int bus = autoCarroMaisProximo[0][0];
        int dia = autoCarroMaisProximo[0][1];
        //Elemento da array Planeamento (que vai corresponder a linha na array distanciasEntreCidades) que representa a cidade a ser comparada.
        int cidadeOrigem = planeamento[bus][dia];
        int KmMaisProximo;
        //verifica se a primeira cidade coincide com a cidade de origem, pois a distância será igual a zero (variável será sempre a menor distância).
        int kmEntreCidades = distanciasEntreCidades[cidadeOrigem][planeamento[0][dia]];
        if (kmEntreCidades != 0) {
            KmMaisProximo = kmEntreCidades;
        } else {
            KmMaisProximo = 1000;
        }
        int busMaisProximo = 0;
        //inicializa com a cidade de origem caso coincida que todos os onibus estejam na mesma cidade no mesmo dia.
        int cidadeMaisProxima = cidadeOrigem;
        //loop para percorrer todos os autocarros do planeamento.
        for (int l = 0; l < planeamento.length; l++) {
            int distancia = distanciasEntreCidades[cidadeOrigem][planeamento[l][dia]];
            if (distancia <= KmMaisProximo && distancia != 0) {
                KmMaisProximo = distancia;
                busMaisProximo = l;
                cidadeMaisProxima = planeamento[l][dia];
            }
        }
        //se todos os autocarros no mesmo dia estiverem na mesma cidade.
        if (KmMaisProximo == 1000) {
            KmMaisProximo = 0;
        }
        gerarLinhaDivisoria('-', 91, "J");
        //System.out.println(" // Autocarro Mais Proximo");
        System.out.printf("No dia <%d>, <Bus%d> estará em <%s>. Bus<%d> é o mais próximo. Está em <%s> a <%d km>%n", dia, bus, obterNomeCidade(cidades, cidadeOrigem), busMaisProximo, obterNomeCidade(cidades, cidadeMaisProxima), KmMaisProximo);
    }

    private static int[][] arrayDistanciasEntreCidades(String fileDistanciasEntreCidades) throws FileNotFoundException {
        Scanner in = new Scanner(new File(fileDistanciasEntreCidades));
        int[][] distanciasEntreCidades = new int[NR_CIDADES][NR_CIDADES];
        for (int x = 0; x < NR_CIDADES; x++) {
            for (int y = 0; y < NR_CIDADES; y++) {
                distanciasEntreCidades[x][y] = in.nextInt();
            }
        }
        in.close();
        return distanciasEntreCidades;
    }

    public static void gerarLinhaDivisoria(char charDivisorio, int tamanhoDaLinha, String letraReferencia) {
        int time = 0;
        // diminuindo 4 do tamanho,  pois se refere aos caracteres da letra topico mais os 2 do "+".
        tamanhoDaLinha = tamanhoDaLinha - 4;
        System.out.print("+");
        while (time < 2) {
            for (int c = 0; c < tamanhoDaLinha / 2; c++) {
                System.out.printf("%c", charDivisorio);
            }
            if (time < 1) {
                System.out.printf("(%s)", letraReferencia);
            }
            time++;
        }
        System.out.println("+");
    }
} Trabalho_Grupo_Aprog {
    
}
