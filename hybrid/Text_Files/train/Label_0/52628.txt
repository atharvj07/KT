import java.util.Scanner;
public class Main{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = Integer.parseInt(sc.next());

		int sum = 0;

		String[] s1 = new String[N];
		int A = 0;
		int B = 0;
		int BA = 0;

		for(int i=0;i<N;i++) {
            int t=0;
			String st = sc.next();
			if(st.substring(0,1).equals("B")) {
				t+=2;
			}
			int sl = st.length();
			if(st.substring(sl-1,sl).equals("A")){
				t++;
			}

			if(t==1) {
				A++;
			}else if(t==2){
				B++;
			}else if(t==3){
				BA++;
			}

			for(int j=0;j<sl-1;j++){

				String t1= st.substring(j,j+2);
				if(t1.equals("AB")) {
					sum++;
					j++;
				}
			}
		}
		if(BA==0) {
			if(B==A) {
				sum += A;
			}else {
				sum += Math.min(A,B);
			}
		}else {
			if(B==A){
				if(A==0) {
					sum += (BA-1);
				}else {
					sum = sum + BA + A;
				}
			}else{
				if(B==0||A==0) {
					sum += BA;
				}else {
					sum += BA + Math.min(A,B);
				}
			}
		}
		System.out.println(sum);
	}
}