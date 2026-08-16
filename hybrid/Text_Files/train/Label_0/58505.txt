import java.util.Scanner;
import java.util.ArrayList;
public class Main{
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		ArrayList<Integer> ex = new ArrayList<Integer>();
		ArrayList<Integer> ey = new ArrayList<Integer>();
		int n = Integer.parseInt(entrada.nextLine());

		for (int i = 0;i < n ;i++ ) {
			int opc = Integer.parseInt(entrada.next().trim());

			if(opc == 1 ){
				ex.add(Integer.parseInt(entrada.next().trim()));
				ey.add(Integer.parseInt(entrada.nextLine().trim()));
			}else{
				
				int t1 = Integer.parseInt(entrada.next().trim());
				int t2 = Integer.parseInt(entrada.next().trim());
				int tam = ex.size();
				boolean[][] bulean = new boolean[tam][tam];

		        for(int k = 0; k<tam; k++)
		            for(int j = 0; j<tam; j++){
		            	int a1 = ex.get(j), a2 = ex.get(k), b1 = ey.get(j), b2 = ey.get(k);
		                if(a1>a2 && a1<b2 || b1>a2 && b1<b2) 
		                	bulean[j][k] = true;
		            }
		        for(int k =0;k<tam; k++)
		            for(int x = 0; x<tam; x++)
		            	for(int j = 0; j<tam; j++){
		                    bulean[x][j] |= (bulean[x][k] &&bulean[k][j]);
		            	}
		        if(bulean[t1-1][t2-1]) 
		        	System.out.println("YES");
		        else 
		        	System.out.println("NO");
			}
		}
	}
}