import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Holiday[] holidays = new Holiday[n];
		for (int i = 0; i < n; i++) {
		    holidays[i] = new Holiday(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt()); 
		}
		int min = Integer.MAX_VALUE;
		for (int i = 1; i <= 360; i++) {
		    int max = 0;
		    for (int j = 0; j < n; j++) {
		        max = Math.max(max, holidays[j].getCrowded(i));
		    }
		    min = Math.min(min, max);
		}
		System.out.println(min);
	}
	
	static class Holiday {
	    int start;
	    int end;
	    int value;
	    
	    public Holiday(int month, int day, int time, int value) {
	        start = (month - 1) * 30 + day;
	        end = start + time - 1;
	        if (end > 360) {
	            end -= 360;
	        }
	        this.value = value;
	    }
	    
	    public int getCrowded(int target) {
	        if (start > end) {
	            if (target <= end || target >= start) {
	                return value;
	            }
	        } else {
	            if (start <= target && target <= end) {
	                return value;
	            }
	        }
	        int v1;
	        if (target < start) {
	            v1 = Math.max(0, value - (start - target));
	        } else {
	            v1 = Math.max(0, value - (360 + start - target));
	        }
	        int v2;
	        if (end < target) {
	            v2 = Math.max(0, value - (target - end));
	        } else {
	            v2 = Math.max(0, value - (360 + target - end));
	        }
	        return Math.max(v1, v2);
	    }
	}
}

