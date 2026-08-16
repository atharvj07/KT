import java.util.*;


public class ProblemC {
    
    
    Scanner in = new Scanner(System.in);
    
    
    void run() {
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        int h = in.nextInt();
        int n = in.nextInt();
        String[] map = new String[h + 2];
        for (int i = 0; i < h; i++) {
            map[i + 1] = '0' + in.next() + '0';
        } // for
        int w = map[1].length() - 2;
        for (map[0] = ""; map[0].length() < w + 2; map[0] += "0");
        map[h + 1] = map[0];
        int[] move = new int[h * w * 8];
        for (int i = 0; i < move.length; i++) {
            move[i] = -1;
        } // for
        
        int curdir = 0;
        int x = 0, y = 0;
        int step = 0;
        while (move[(y * w + x) * 8 + curdir] == -1) {
            move[(y * w + x) * 8 + curdir] = step++;
            char cur = map[y + 1].charAt(x + 1);
            //System.out.println(cur + " " + step);
            int xx = x, yy = y;
            do {
                xx += dx[curdir % 4];
                yy += dy[curdir % 4];
            } while(map[yy + 1].charAt(xx + 1) == cur);
            xx -= dx[curdir % 4];
            yy -= dy[curdir % 4];
            int cdir = ((curdir % 4) + (curdir >= 4 ? 1 : 3)) % 4;
            do {
                xx += dx[cdir % 4];
                yy += dy[cdir % 4];
            } while(map[yy + 1].charAt(xx + 1) == cur);
            xx -= dx[cdir % 4];
            yy -= dy[cdir % 4];
            xx += dx[curdir % 4];
            yy += dy[curdir % 4];
            if (map[yy + 1].charAt(xx + 1) == '0') {
                xx -= dx[curdir % 4];
                yy -= dy[curdir % 4];
                if (curdir < 4) {
                    curdir += 4;
                } else {
                    curdir = (curdir + 1) % 4;
                } // else
            } else {
                x = xx;
                y = yy;
            } // else
        } // while
        int start = move[(y * w + x) * 8 + curdir];
        int loop = step - move[(y * w + x) * 8 + curdir];
        n = (n - start) % loop + start;
        for (int i = 0; i < move.length; i++) {
            if (move[i] == n) {
                int p = i / 8;
                System.out.println(map[p / w + 1].charAt(p % w + 1));
                return;
            } // if
        } // for
    } // run
    
    public static void main(String... args) {
        (new ProblemC()).run();
    } // args
    
    
} // class ProblemC
