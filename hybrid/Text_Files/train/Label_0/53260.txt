import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<P> pp = new ArrayList<>();
        int k = 0;
        for (int i = 0;i < n;++i){
            int[] ps = {sc.nextInt(),sc.nextInt(),sc.nextInt()};
            Arrays.sort(ps);
            P p = new P(ps[0],ps[1],ps[2]);
            if(pp.contains(p)){
                ++k;
            }
            else pp.add(p);
        }
        System.out.println(k);
    }

    static class P{
        int p1,p2,p3;

        public P(int p1,int p2,int p3){
            this.p1 = p1;this.p2 = p2;this.p3 = p3;
        }

        @Override
        public boolean equals(Object obj) {
            P p = (P)obj;
            if(p.p1 == this.p1&&p.p2 == this.p2&&p.p3 == this.p3)return true;
            return false;
        }
    }

}

