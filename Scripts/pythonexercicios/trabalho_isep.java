import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Ex_01 {
    static Scanner ler = new Scanner(System.in);
    static final String FILE1 = "samplefile1.txt"; // Constante para nome dos arquivos.
    static final String LIST = "list.txt";

    public static void main(String[] args) throws FileNotFoundException {
        usingPrintWriter();
        usingScanner();
        readRowsFiles(LIST);
        readShopValues();
        totalGastoNaSeccao("Frutas");
        totalGastoNasCompras();
        criaGravaFicheiro();
        readRowsFiles("list2.txt");
    }

    private static void criaGravaFicheiro() throws FileNotFoundException {
        PrintWriter out = new PrintWriter(new File("list2.txt"));

        String[] arr1 = {"frutas", "bebidas", "bebidas ", "talho" };
        String[] arr2 = {"banana", "sumol ", "fanta", "costeleta" };
        double[] arr3 = {1.2, 2, 6, 0.75};
        double[] arr4 = {3.1, 1.45, 3.99, 5.99};
        for (int item = 0; item < 4; item++) {
            out.printf("%d %s %s %f %.2f%n", (item + 1), arr1[item], arr2[item], arr3[item], arr4[item]);
        }
        out.close();
    }

    private static void totalGastoNasCompras() throws FileNotFoundException {
        Scanner in = new Scanner(new File(LIST));
        double totalGastoNasCompras = 0;

        String linha = in.nextLine();   // ignora a linha do cabeçalho.
        while (in.hasNextLine()) {
            linha = in.nextLine();
            String[] itensDaLista = linha.split(" ");
            totalGastoNasCompras += Double.parseDouble(itensDaLista[4]);
        }
        in.close();
        System.out.printf("Total gasto nas compras; €%.2f%n", totalGastoNasCompras);
        linha();


    }

    private static void totalGastoNaSeccao(String secao) throws FileNotFoundException {
        Scanner in = new Scanner(new File(LIST));

        String linha;
        double total = 0;

        while (in.hasNextLine()) {
            linha = in.nextLine();
            String[] itensDaLinha = linha.split(" ");
            if (secao.equals(itensDaLinha[1])) {
                total += Double.parseDouble(itensDaLinha[4]);
            }
        }
        in.close();
        System.out.println("Secão " + secao + ". total gasto: €" + total);
        linha();
    }

    private static void linha() {
        for (int x = 0; x < 40; x++) {
            System.out.print("-");
        }
        System.out.println();
    }

    private static void readShopValues() {

        String line = "1 Mercearia Arroz 2 5,99";
        String[] itensDaLinha = line.split(" ");
        for (String item : itensDaLinha) {
            System.out.println(item);
        }
        linha();
    }

    private static void readRowsFiles(String file) throws FileNotFoundException {
        Scanner in = new Scanner(new File(file));

        //String line = in.nextLine(); // ignora a linha do cabeçalho.
        while (in.hasNextLine()) {
            String line = in.nextLine();
            System.out.println(line);
        }
        linha();
        in.close();
    }

    public static void usingPrintWriter() throws FileNotFoundException {
        String fileContent = "Hello . Welcome to APROG.";

        PrintWriter printWriter = new PrintWriter(FILE1); // cria o arquivo txt.

        String row = ler.nextLine();
        printWriter.print(fileContent);                //inseri na 1ª linha a string
        printWriter.println();                         // pula uma linha
        printWriter.printf("%d in a %s%n", 24, "row"); // usa o printf para formatar a 3ª linha.
        printWriter.println(row);   // insere na linha do arquivo o imput do usuario.

        printWriter.close();  // fecha o arquivo.
        linha();
    }

    public static void usingScanner() throws FileNotFoundException {

        Scanner ler = new Scanner(new File(FILE1)); //vai ler dados de um arquivo já existente.

        while (ler.hasNextLine()) // ler linha a linha enquanto tiver linha com elementos.
            System.out.println(ler.nextLine());
        /*System.out.println(ler.nextLine());
        System.out.println(ler.nextInt());
        System.out.println(ler.next());
        System.out.println(ler.nextLine());
        System.out.println(ler.nextLine());*/
        linha();
        ler.close();
    }
}
/*
// Visualizar apenas para verificas os dados das matrizes-----------
        gerarLinhaDivisoria('-', 31, "*");
        System.out.println(" // Array AutoCarro Mais Proxino.");
        for (int i = 0; i < 1; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(autoCarroMaisProximo[i][j] + " ");
            }
            System.out.println();
        }
        gerarLinhaDivisoria('-', 31, "*");
        System.out.println(" // Array distancias Entre As Cidades.");
        for (int[] distanciasEntreCidade : distanciasEntreCidades) {
            for (int j = 0; j < distanciasEntreCidades[0].length; j++) {
                System.out.printf("%5d", distanciasEntreCidade[j]);
            }
            System.out.println();
        }
        // ------------------------------------------------------------------*/ 
