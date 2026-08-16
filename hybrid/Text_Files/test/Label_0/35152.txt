import java.util.Scanner;


public class Main {
    
    boolean[][] map;
    
    void run() {
        Scanner sc = new Scanner(System.in);
        sc.next();
        int t = 1;
        while (sc.hasNext()) {
            map = new boolean[8][8];
            
            for (int y = 0; y < 8; y++) {
                String l = sc.next();
                for (int x = 0; x < 8; x++) {
                    map[y][x] = l.charAt(x) - '0' == 1;
                }
            }
            
            dfs(sc.nextInt() - 1, sc.nextInt() - 1);
            System.out.println("Data " + t++ + ":");
            for (int y = 0; y < 8; y++) for (int x = 0; x < 8; x++) {
                System.out.print((map[y][x] ? '1' : '0') + (x == 7 ? "\n" : ""));
            }
        }
    }
    
    int[] dx = {-1,0,1,0}, dy = {0,-1,0,1};
    void dfs(int x, int y) {
        map[y][x] = false;
        
        for (int i = 0; i < 4; i++) {
            for (int nx = x, ny = y, c = 0; !out(nx, ny) && c <= 3; c++) {
                if (map[ny][nx]) dfs(nx, ny);
                nx += dx[i]; ny += dy[i];
            }
        }
    }
    
    boolean out(int x, int y) {
        return x < 0 || y < 0 || x >= 8 || y >= 8;
    }
    
    public static void main(String[] args) {
        new Main().run();
    }
}