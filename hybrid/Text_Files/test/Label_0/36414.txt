import java.util.Scanner;

public class Main{
    
    int HEIGHT = 4;
    int WIDTH = 4;
    int[][] relationXY;

    void run(){
        Scanner sc = new Scanner(System.in);
        //int[][] temp = { { -2, 1},{ -1, 1},{ 1, 1},{ 1, 2}};
        
        while(true){
            int[][] temp = new int[4][2];
            int x = sc.nextInt();
            if(x > 4){
                break;
            }
            int y = sc.nextInt();
            temp[0][0] = x;
            temp[0][1] = y;
            for(int i = 1;i < 4;i++){
                temp[i][0] = sc.nextInt();
                temp[i][1] = sc.nextInt();
            }
            relationXY = temp;
            boolean[][] visited = new boolean[HEIGHT][WIDTH];
            System.out.println(dfs(visited,HEIGHT*WIDTH,0));
        }
    }
    int dfs(boolean[][] visited,int remain,int next){
        /*
        System.out.println("remain "+remain);
        for(int i = 0;i < HEIGHT;i++){
            for(int ii = 0;ii < WIDTH;ii++){
                System.out.print(visited[i][ii]? 1: 0);
            }
            System.out.println();
        }
        */
        if(remain == 0){
            return 1;
        }
        if(next >= HEIGHT*WIDTH){
            return 0;
        }

        int count = 0;

        int y = next / HEIGHT;
        int x = next % WIDTH;
        if( visited[y][x]){
            count+=dfs(visited,remain,next+1);
        }
        else{
            for(int i = 0;i < relationXY.length;i++){
                int rx = x + relationXY[i][0];
                int ry = y + relationXY[i][1];
                if(rx < 0 || WIDTH <= rx || ry < 0 || HEIGHT <= ry){
                    continue;
                }
                if(!visited[ry][rx]){
                    visited[y][x] = true;
                    visited[ry][rx] = true;
                    count += dfs(visited,remain-2,next+1);
                    visited[y][x] = false;
                    visited[ry][rx] = false;
                }
            }
        }

        return count;
    }
    public static void main(String[] args) {
        new Main().run();
    }
}
    