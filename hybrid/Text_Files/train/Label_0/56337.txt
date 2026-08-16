import java.util.*;

public class B {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int count = in.nextInt();
    int me = in.nextInt()-1;
    int[] map = new int[count];
    int[] reverseMap = new int[count];
    Arrays.fill(reverseMap,-1);
    for(int i=0;i<count;++i) {
      map[i] = in.nextInt()-1;
      if (map[i] != -1) {
        reverseMap[map[i]] = i;
      }
    }
    HashMap<Integer, Integer> cycles = new HashMap<Integer, Integer>();
    boolean[] done = new boolean[count];
    boolean isUs = false;
    int ourLength = 0;
    int ourLoc = 0; // how many people are behind us?
    // so our location from the front is ourLength-ourLoc, right? yes.
    for(int i=0;i<count;++i) {
      isUs = false;
      if (done[i]) continue;
      done[i] = true;
      int cur = i;
      if (reverseMap[i] == -1 && map[i] == -1) {
        if (cur == me) {
          ourLength = 1;
          ourLoc = 0;
        } else {
          if (cycles.containsKey(1)) {
            cycles.put(1,cycles.get(1)+1);
          } else {
            cycles.put(1,1);
          }
        }
      } else {
        while(reverseMap[cur] != -1) {
          cur = reverseMap[cur];
        }
        int cycleLength = 1;
        done[cur] = true;
        if(cur == me) {
          isUs = true;
          ourLoc = 0;
        }
        while(map[cur] != -1) {
          cur = map[cur];
          done[cur] = true;
          ++cycleLength;
          if(cur == me) {
            isUs = true;
            ourLoc = cycleLength-1;
          }
        }
        if (isUs) {
          ourLength = cycleLength;
        } else {
          if (cycles.containsKey(cycleLength)) {
            cycles.put(cycleLength,cycles.get(cycleLength)+1);
          } else {
            cycles.put(cycleLength,1);
          }
        }
      }
    }
    // shit two cases: we are at a 0 or we aren't.
    // if we aren't at a 0 we need to know what cycle we're in
    // now that we have all the cycles, we need to know what's possible
    // System.err.println(ourLength + " " + ourLoc);
    // System.err.println(cycles);
    boolean[] dp = new boolean[count+1];
    Arrays.fill(dp, false);
    dp[0] = true;
    for(int key : cycles.keySet()) {
      for(int z=0;z<cycles.get(key);++z) {
        for(int i=count;i>=key;--i) {
          dp[i] = (dp[i]||dp[i-key]);
        }
      }
      // System.err.println(Arrays.toString(dp));
    }
    for(int i=0;i<count;++i) {
      if (dp[i]) {
        System.out.println(i+(ourLength-ourLoc));
      }
    }
  }
}
