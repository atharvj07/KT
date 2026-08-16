import java.util.Scanner;
public class Young_Physicist {
    private static final Scanner SCANNER = new Scanner(System.in);

    public static void main(String[] args) {
        int round=0,sum_x=0,sum_y=0,sum_z=0;
        int []number=new int[300];
        round=SCANNER.nextInt();
        for(int i=0;i<round*3;++i){
            number[i]=SCANNER.nextInt();
        }
        for(int i=0;i<round*3;i=i+3){
            sum_x+=number[i];
            sum_y+=number[i+1];
            sum_z+=number[i+2];
        }
        if(sum_x==0&&sum_y==0&&sum_y==0){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
    }
}
