import java.util.Scanner;

public class Drox_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingresa un numero para hacer la comprobacion:");
        int n = sc.nextInt();

        int resultado = compruebaNumero(n);

        switch (resultado) {
            case 0:
                System.out.println("El numero es fibonacci");
                break;
            case 1:
                System.out.println("El numero es primo");
                break;
            case 2:
                System.out.println("El numero es par");
                break;
            default:
                System.out.println("El numero no es ni primo ni par, ni fibonacci");
                break;
        }
    }

    public static int compruebaNumero(int numero) {
        int resultado = 0;

        if (esFibonacci(numero)) {
            resultado = 0;
        } else if (esPrimo(numero)) {
            resultado = 1;
        } else if (esPar(numero)) {
            resultado = 2;
        }

        return resultado;
    }

    public static boolean esFibonacci(int numero) {
        boolean resultado = false;

        return resultado;
    }

    public static boolean esPrimo(int numero) {
        boolean resultado = false;
        return resultado;
    }

    public static boolean esPar(int numero) {

        if (numero % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }
}