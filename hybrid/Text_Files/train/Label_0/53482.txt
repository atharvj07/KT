import java.util.Arrays;
import java.util.Scanner;

public class Main{
    static Scanner s = new Scanner(System.in);
    static class calendarSystem implements Comparable<calendarSystem>{
        String EraName;
        int EraBasedYear;
        int WesternYear;

        calendarSystem(String eraName, int eraBasedYear, int westernYear) {
            EraName = eraName;
            EraBasedYear = eraBasedYear;
            WesternYear = westernYear;
        }

        public int compareTo(calendarSystem x){
            return this.WesternYear-x.WesternYear;
        }

    }

    public static void main(String[] args) {
        while(true){
            int N = s.nextInt();
            int Q = s.nextInt();
            if(N==0 && Q==0) break;
            calendarSystem[] eraYear = new calendarSystem[N];

            for(int i=0;i<N;i++){
                String  EraName = s.next();
                int EraBasedYear = s.nextInt();
                int WesternYear = s.nextInt();

                eraYear[i] = new calendarSystem(EraName,EraBasedYear,WesternYear);
            }
            Arrays.sort(eraYear);

            for(int i=0;i<Q;i++){
                int Query = s.nextInt();

                convertingYear(Query,eraYear);
            }
        }
    }
    static void convertingYear(int Query,calendarSystem[] eraYear){
        for(int i=0;i<eraYear.length;i++){
            int WesternYear = eraYear[i].WesternYear;
            int EraBasedYear = eraYear[i].EraBasedYear;
            String EraName = eraYear[i].EraName;

            if(Query<=WesternYear && Query>=WesternYear-EraBasedYear+1){
                int Year = EraBasedYear-(WesternYear-Query);
                System.out.println(EraName+" "+Year);
                return;
            }
        }
        System.out.println("Unknown");
    }
}