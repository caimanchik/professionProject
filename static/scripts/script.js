let loc = document.location

if (loc.href.indexOf('demand') > 0)
    document.querySelector('.demand').classList.add('selected')
else if (loc.href.indexOf('geography') > 0)
    document.querySelector('.geo').classList.add('selected')
else if (loc.href.indexOf('skills') > 0)
    document.querySelector('.skills').classList.add('selected')
else if (loc.href.indexOf('latest') > 0)
    document.querySelector('.latest').classList.add('selected')
else
    document.querySelector('.home').classList.add('selected')
