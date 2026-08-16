import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);

		while(true){
			int n = stdIn.nextInt();
			int m = stdIn.nextInt();
			if(n+m==0){
				return;
			}
			int[] taro = new int[n];
			int taroSum = 0;
			for(int i=0;i<n;i++){
				taro[i] = stdIn.nextInt();
				taroSum+=taro[i];
			}
			int[] hana = new int[m];
			int hanaSum = 0;
			for(int i=0;i<m;i++){
				hana[i] = stdIn.nextInt();
				hanaSum+=hana[i];
			}
			int changeSumMin = -1;
			int taroChange = -1;
			int hanaChange = -1;
			for(int i=0;i<n;i++){
				for(int j=0;j<m;j++){
					int taroAfter = taroSum-taro[i]+hana[j];
					int hanaAfter = hanaSum-hana[j]+taro[i];
					if(taroAfter==hanaAfter){
						int changeSum = taro[i]+hana[j];
						if(changeSumMin==-1||changeSum<changeSumMin){
							changeSumMin = changeSum;
							taroChange = taro[i];
							hanaChange = hana[j];
						}
					}
				}
			}
			if(changeSumMin!=-1){
				System.out.println(taroChange+" "+hanaChange);
			}
			else{
				System.out.println("-1");
			}
		}
	}
}