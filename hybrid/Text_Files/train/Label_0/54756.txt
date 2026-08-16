import java.util.*;

class Main{

    void solve(){
        Scanner sc = new Scanner(System.in);

        while(true){
            int target = sc.nextInt();
            int sheet = sc.nextInt();
            if(target==0 && sheet==0) break;

            int n = 0;
            while(sheet>Math.pow(10,n+1)) n++;
            n++;

            int[] list = new int[n];
            int sheet2 = sheet;
            for(int i=n-1; i>=0; i--){
                list[i] = sheet2%10;
                sheet2 /= 10;
            }

            int max = -1;
            String parts = "";
            for(int mask=1; mask<1<<n; mask+=2){
                int sum = 0;
                int num = -1;
                String tmp = "";
                for(int j=0; j<n; j++){
                    if((mask&(1<<j))>0){
                        if(num!=-1){
                            sum += num;
                            tmp += String.valueOf(num) + " ";
                        }
                        num = list[j];
                    }else{
                        num *= 10;
                        num += list[j];
                    }
                }
                sum += num;
                tmp += String.valueOf(num);

                if(sum==max) parts = "";
                if(sum>max && sum<=target){
                    max = sum;
                    parts = tmp;
                }

            }

            if(max==-1) System.out.println("error");
            else if(parts.equals("")) System.out.println("rejected");
            else System.out.println(max+" "+parts);     
        }
    }

    public static void main(String[] args){
        new Main().solve();
    }
}