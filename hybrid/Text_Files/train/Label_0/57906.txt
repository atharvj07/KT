import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int[] c1 = new int[1001];
        int[] c2 = new int[1001];
        while(true){
            String s = sc.nextLine();
            if(s.equals(""))break;
            c1[Integer.parseInt(s.split(",")[0])]++;
        }
        while(sc.hasNext()){
            c2[Integer.parseInt(sc.nextLine().split(",")[0])]++;
        }
        sc.close();
        for(int i = 0; i <= 1000; i++) {
        	if(c1[i] != 0 && c2[i] != 0) {
        		System.out.printf("%d %d\n", i, c1[i] + c2[i]);
        	}
        }
	}
}
