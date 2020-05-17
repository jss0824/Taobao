cookie ={}
b = 'x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=16dedb6e4315bf-0570a50a09a925-e343166-1fa400-16dedb6e43279a; t=ddfbf9e1821a599beab74786b4fadb05; _m_h5_tk=c861ed63ba4becf367d785a9882c03fb_1584612398381; _m_h5_tk_enc=ea51611fc8f47d0503f7ceb17d1094f5; cna=4BJsFi1P7RUCAXvEC6I3DD9I; enc=T8ih5DzVwwXiRQv1qhIsQdc0y1q5emWWdTYqTeoDNSKNpxY53t12yJHaQgqu749i8rwo9Fpvu2ZcC6513beVlQ%3D%3D; sgcookie=E%2F1%2B6HAwzWHydHwwvF7b1; uc3=nk2=1rQRXbulApU%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxd9kq6J6iW07g6A%3D&id2=VAKMd4fpjh7G; lgc=%5Cu8776%5Cu821E%5Cu98CE%5Cu6F47; uc4=id4=0%40VhvAhRvxDXGpsHeKm3kEayz0iAs%3D&nk4=0%401AVyc9eZ0fHE6xQ72%2BBqNijEZA%3D%3D; tracknick=%5Cu8776%5Cu821E%5Cu98CE%5Cu6F47; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; tfstk=coZCBAAw1BAQKJDB8z6Z4h7T00i5ZnpjFwG3dPMmfaHHKxwCimKqGDX4rQKtkA1..; mt=ci=20_1; v=0; cookie2=5b42156697d899cb8530db62a9ff132e; _tb_token_=e31137be68653; uc1=cookie14=UoTUPvnayHSLWw%3D%3D; JSESSIONID=2FB64F3C4BC83BFA1E57407D59138044; l=dBxtlIEVQ1891CB6BOfi5JmH9kQtnKRf5sPr-0SSMIB1tTWKIdkvoHwE4ZqW63QQEtfAbetPgrrGARhH5fzLRxgKqelyRs5mp9p6y; isg=BI6ORGlpXIGq3-iuzPIsFKmX32RQD1IJmyNOZ7jffBX-Gyd1IJ3SGdidU0d3A0oh'
for line in b.split(';'):

    key,value = line.split('=',1)

    cookie[key.strip()] = value

print(cookie)