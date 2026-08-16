import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while(cin.hasNext()){
			int[][] a = new int[1000][2];
			int count=0;
			int max = 0;
			while(true){
				a[count][0]=cin.nextInt();
				a[count][1]=cin.nextInt();
				if(a[count][0]+a[count][1]==0){
					break;
				}
				max = Math.max(Math.max(max, a[count][0]),a[count][1]);
				count++;
			}
			max++;
			int edgeCount=count;
			int[][] field = new int[max][max];
			for(int i = 0; i < count;i++){
				field[a[i][0]][a[i][1]]++;
				field[a[i][1]][a[i][0]]++;
				//System.out.println(a[i][0]+" " + a[i][1]);
			}
			int i;
			for(i = 1; i < field.length;i++){
				int edge=0;
				for(int j = 1; j < field.length;j++){
					//System.out.print(field[i][j]);
					edge+=field[i][j];
				}
				
				//System.out.println(edge);
				if(i==1||i==2){
					if(edge%2==0){
						System.out.println("NG");
						break;
					}
				}
				else{
					if(edge%2==1){
						System.out.println("NG");
						break;
					}
				}
			}
			if(i==field.length)
				System.out.println("OK");
			
		}
	}

}