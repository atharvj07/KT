import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Calendar;
import java.util.StringTokenizer;
import java.util.TimeZone;


public class Main {

    public static int sec,minute,hour,day,week,month;

    public static void main(String args[]) throws Exception {

        BufferedReader buf=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s=new StringTokenizer(buf.readLine());

        sec = Integer.parseInt(s.nextToken());
        minute = Integer.parseInt(s.nextToken());
        hour = Integer.parseInt(s.nextToken());
        week = Integer.parseInt(s.nextToken());
        day = Integer.parseInt(s.nextToken());
        month = Integer.parseInt(s.nextToken());

        if (week != -1) {
            week++; if (week==8) week=1;
        }

        s=new StringTokenizer(buf.readLine());
        int n = Integer.parseInt(s.nextToken());
        for(int i=0;i<n;i++) {
            s=new StringTokenizer(buf.readLine());
            long x = Long.parseLong(s.nextToken());
            cal(x);
        }
    }

    public static boolean isR(Calendar c) {
        int y = c.get(Calendar.YEAR);
        return y%400==0 || (y%100!=0 && y%4==0);
    }

    public static boolean ck(Calendar c) {
        if (month != -1 && month-1 != c.get(Calendar.MONTH)) return false;
        if (day != -1 || week != -1) {
            if (c.get(Calendar.DAY_OF_MONTH) != day && c.get(Calendar.DAY_OF_WEEK) != week) return false;
        }
        if (hour != -1 && c.get(Calendar.HOUR_OF_DAY) != hour) return false;
        if (minute != -1 && c.get(Calendar.MINUTE) != minute) return false;
        if (sec!=-1 &&  c.get(Calendar.SECOND) != sec) return false;
        return true;
    }

    public static void cal(long x) {
        x++;
        x *= 1000;
        Calendar c = Calendar.getInstance();
        c.setTimeInMillis(x); c.setTimeZone(TimeZone.getTimeZone("UTC"));
        if (month==2 &&  day==29 && week==-1) {
            while (!isR(c)) {
                c.add(Calendar.YEAR, 1);
                c.set(Calendar.MONTH, 0);
                c.set(Calendar.DAY_OF_MONTH, 1); c.set(Calendar.HOUR_OF_DAY, 0);
                c.set(Calendar.MINUTE,0); c.set(Calendar.SECOND, 0);
            }
        }
        if (month != -1) {
            while(c.get(Calendar.MONTH) != month-1) {
                c.add(Calendar.MONTH, 1);
                c.set(Calendar.DAY_OF_MONTH, 1); c.set(Calendar.HOUR_OF_DAY, 0);
                c.set(Calendar.MINUTE,0); c.set(Calendar.SECOND, 0);
            }
        }
        if (day != -1 || week != -1) {
            while(true) {
                if (c.get(Calendar.DAY_OF_MONTH) == day) break;
                if (c.get(Calendar.DAY_OF_WEEK) == week) break;
                c.add(Calendar.DAY_OF_MONTH, 1);
                c.set(Calendar.HOUR_OF_DAY, 0);
                c.set(Calendar.MINUTE,0); c.set(Calendar.SECOND, 0);
            }
        }
        if (hour != -1) {
            while(true) {
                if (c.get(Calendar.HOUR_OF_DAY) == hour) break;

                c.add(Calendar.HOUR_OF_DAY, 1);
                c.set(Calendar.MINUTE,0); c.set(Calendar.SECOND, 0);
            }
        }
        if (minute != -1) {
            while(true) {
                if (c.get(Calendar.MINUTE) == minute) break;
                c.add(Calendar.MINUTE, 1);
                c.set(Calendar.SECOND, 0);
            }
        }
        if (sec != -1) {
            while(true) {
                if (c.get(Calendar.SECOND) == sec) break;
                c.add(Calendar.SECOND, 1);
            }
        }
        if (ck(c)) System.out.println(c.getTimeInMillis() / 1000);
        else cal(c.getTimeInMillis()/1000);
    }
}
