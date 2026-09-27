class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> h=new HashMap<Character,Integer>(); 
        if(s.length()==0) return 0;
        int long1=0;
        boolean flag=true;
        for(int i=0;i<s.length();i++)
        for(int j=i;j<s.length();j++)
        {
        char[] sub = s.substring(i,j+1).toCharArray();
        for(int m=0;m<sub.length;m++)
        {
            h.put(sub[m],h.getOrDefault(sub[m],0)+1);
        }
        for(int x : h.values())
        {
            if(x>1)
            {   
                flag=false;
                break;
            }
            else{
                flag=true;
            }
        }
        if(flag==true && long1<sub.length)
        {
            long1=sub.length;
        }
         h.clear();
        
        }
        return long1;
    }
}
