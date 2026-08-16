import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int t =scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n=scanner.nextInt();
            int k=scanner.nextInt();
            int[] visit=new int[200];
            int count=0; //记录不同大小的数字个数
            for (int j = 0; j < n; j++) {
                int num=scanner.nextInt();
                if(visit[num]==0){
                    visit[num]=1; count++;
                }
            }
            if(k==1 && count!=1) System.out.println(-1); //数字种类大于k无解
            else if(k==1 && count==1) System.out.println(1); //只有一种数字
            else if(count<=k) System.out.println(1); //数字种类小于k，不需要分解数字
            //对于每个b数组有k个不同数。
            //那么第一个b数组可以消灭掉前k个数，之后每个b数组依次消灭后面(k-1)个数（最前面是0）
            else
                System.out.println(1+(count-2)/(k-1));

        }
    }
}

 	 	  	  	 	   		 				    		  	