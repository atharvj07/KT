import java.io.IOException;
import java.util.Scanner;
public class SerejaAndDima {

	public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(System.in);
		
		short n = s.nextShort();
		short card[] = new short[n];
		short i, j;
		for (i=0; i<n; i++) {
			card[i] = s.nextShort();
		}
		
		int S=0, D=0;
		i = 0;
		j = (short) (n-1);
		while(n>0) {
			if (card[i]>card[j]) {
				S+=card[i];
				card[i] = 0;
				i++;
			}
			else {
				S+=card[j];
				card[j] = 0;
				j--;
			}
			n--;
			if (n==0) break;
			if (card[i]>card[j]) {
				D+=card[i];
				card[i] = 0;
				i++;
			}
			else {
				D+=card[j];
				card[j] = 0;
				j--;
			}
			n--;
		}
		System.out.println(S+" "+D);

	}

}
