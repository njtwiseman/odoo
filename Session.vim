let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/shopMgmt/odoo
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd addons/auto_service_shop/models/vehicle.py
set stal=2
tabnew
tabrewind
edit fugitive:///home/nick/shopMgmt/odoo/.git//b17428a6087693e33b5e82b91c6c5544039691a0/addons/auto_service_shop/views/auto_service_views.xml
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 248 + 140) / 280)
argglobal
enew
file NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=10
setlocal nofen
wincmd w
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=10
setlocal nofen
let s:l = 1 - ((0 * winheight(0) + 35) / 70)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 140) / 280)
exe 'vert 2resize ' . ((&columns * 248 + 140) / 280)
tabnext
edit addons/auto_service_shop/security/ir.model.access.csv
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=10
setlocal nofen
let s:l = 21 - ((20 * winheight(0) + 35) / 70)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
21
normal! 069|
tabnext 1
set stal=1
badd +1 addons/auto_service_shop/models/service_ticket.py
badd +62 addons/auto_service_shop/models/vehicle.py
badd +22 addons/auto_service_shop/security/ir.model.access.csv
badd +83 addons/auto_service_shop/models/auto_service.py
badd +3 addons/auto_service_shop/views/vehicle_action.xml
badd +5 addons/auto_service_shop/views/vehicle_template.xml
badd +7 addons/auto_service_shop/views/vehicle_views.xml
badd +33 addons/auto_service_shop/__manifest__.py
badd +4 addons/auto_service_shop/security/security.xml
badd +0 addons/auto_service_shop/5
badd +76 addons/auto_service_shop/views/auto_service_views.xml
badd +0 fugitive:///home/nick/shopMgmt/odoo/.git//b17428a6087693e33b5e82b91c6c5544039691a0/addons/auto_service_shop/views/auto_service_views.xml
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOSc
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
