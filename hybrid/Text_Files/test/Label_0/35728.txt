import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
	GgXelXÉw×I n < 2^15@¾©çÅ«½±ÆBÅ©¢ÆÊ
*/
//public class Problem1200_GoldbachsConjecture {
public class Main {
	private PrimeMaster primeMaster;
	public static void main(String[] args) {
		try {
		//	Problem1200_GoldbachsConjecture test = new Problem1200_GoldbachsConjecture();
			Main test = new Main();
			
			BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
			
			String line;
			while((line = reader.readLine()) != null) {
				int target = Integer.parseInt(line);
				if(target < 4) {
					break;
				} else {
					test.showAnswer(target);
				}
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
//	Problem1200_GoldbachsConjecture() {
	Main() {
		primeMaster = new PrimeMaster();
	}
	void showAnswer(int number) {
		int answerNumber = 0;
		
		int counterpart = number-2;
		if(primeMaster.isPrime(counterpart)) {
			answerNumber++;
		}
		for(int i = 3; i <= number/2; i += 2) {
			counterpart = number - i;
			if(primeMaster.isPrime(i) && primeMaster.isPrime(counterpart)) {
				answerNumber++;
			//	System.out.println(i + " + " + counterpart);
			}
		}
		
		System.out.println(answerNumber);
	}
	private class PrimeMaster {
		final private boolean[] SIEVE;	//RÈãÌïÉÂ¢ÄA(n-1)/2 Å¾çêélÌêªtrueÈçfBfalseÈçï
		
		PrimeMaster() {
			SIEVE = createSieve();
		}
		private boolean[] createSieve() {
			boolean[] sieve = new boolean[(int)(Math.pow(2,14))];
			Arrays.fill(sieve, true);
			
			for(int i = 1; i < sieve.length/2; i++) {
				if(sieve[i] == true) {	//sieve[1] = true@ÈçRªfÅRÌ{Í [1+3a] ÌÊuÉ¶Ý·é
										/*
										n1 = (x-1)/2	n1 = (3-1)/2 = 1
										na = (ax-1)/2	n5 = (3*5-1)/2 = 7
										
										na - n1 = ((a-1)*x)/2	:n5-n1 = 6 = 3*((5-1)/2)
										a = 1,3,5,7c ÌÆ«
										na-n1 = 0,x,2x,3x,4xc Æ±­
										sieve[a] Ì{ÌlÌ b{(bÍï)Í sieve[a + bx] Ì{Ìl
										*/
					int trueNumber = i*2 + 1;
					for(int j = i + trueNumber; j < sieve.length; j += trueNumber) {
						sieve[j] = false;
					}
				}
			}
			
			return sieve;
		}
		private boolean isPrime(int number) {
			if(number == 2) {
				return true;
			}
			if(number % 2 == 0 || number == 1) {
				return false;
			}
			return SIEVE[(number-1)/2];
		}
	}
}