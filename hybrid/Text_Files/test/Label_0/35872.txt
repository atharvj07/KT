import java.util.Scanner;

public class Placar4{
    public final static int MAX_N=10000;

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        long [] quadrados = new long[MAX_N+1];
        for (int i=0;i<=MAX_N;i++){
            quadrados[i]=i*i;
        }
        int num_triangulos=0;

        int n = scanner.nextInt();

        int a=1;
        while (a<=n){
            int b=a+1;
            while (b<=n){
                int soma_catetos_quadrados=a*a + b*b;
                if (soma_catetos_quadrados<=n*n){
                    int raiz = (int) Math.sqrt(soma_catetos_quadrados);
                    if (quadrados[raiz]==soma_catetos_quadrados){
                        num_triangulos++;
                    }
                }
                b++;
            }
            a++;
        }

        System.out.println(num_triangulos);
    }
}
	  			 	 		 	 			   	    		 			