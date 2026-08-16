import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static String Sleep(int hh, int mm, int hh2, int mm2) {
        int hhr, mmr = 0;

        if (hh == 0)
            hh = 24;

        mmr = mm - mm2;

        hhr = hh - hh2;

        if (mmr < 0) {
            mmr = 60 + mmr;
            hhr--;
        }

        if (hhr < 0)
            hhr = 24 + hhr;

        if (hhr == 24)
            hhr = 0;

        String res = (hhr == 24) ? "00:" : (hhr <= 9) ? "0" + hhr + ":" : hhr
                + ":";

        res += (mmr == 0) ? "00" : (mmr <= 9) ? "0" + mmr : mmr;

        return res;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] test = bf.readLine().split(":");

        int hh = Integer.parseInt(test[0]);
        int mm = Integer.parseInt(test[1]);

        String[] test2 = bf.readLine().split(":");

        int hh2 = Integer.parseInt(test2[0]);
        int mm2 = Integer.parseInt(test2[1]);

        System.out.println(Sleep(hh, mm, hh2, mm2));

    }
}