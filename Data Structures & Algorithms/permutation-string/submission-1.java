class Solution {
    ArrayList<String> l = new ArrayList<String>();
    public boolean checkInclusion(String s1, String s2) {
        for(int i=0;i<s2.length();i++)
        for(int j=i;j<s2.length();j++)
        l.add(s2.substring(i,j+1));    
      char[] m1=s1.toCharArray();
      Arrays.sort(m1);    
      String sorted=new String(m1);
   for(int m=0;m<l.size();m++)
   {
     char[] s=l.get(m).toCharArray();
     Arrays.sort(s);
      String sub=new String(s);
     
     if(sub.equals(sorted))
     return true;
     
    }
     return false;
    }
}
