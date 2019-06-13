let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/shopMgmt/odoo/addons/auto_service_shop
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd models/vehicle.py
edit NERD_tree_1
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=10
setlocal nofen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 35) / 71)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
tabnext 1
badd +45 __manifest__.py
badd +9 models/vehicle.py
badd +0 NERD_tree_1
badd +21 security/ir.model.access.csv
badd +1 models/service_ticket.py
badd +83 models/auto_service.py
badd +8 views/vehicle_action.xml
badd +5 views/vehicle_template.xml
badd +29 views/vehicle_views.xml
badd +4 security/security.xml
badd +1 5
badd +76 views/auto_service_views.xml
badd +4 views/view.xml
badd +1 static/description/web-icon.png
badd +220 ~/shopMgmt/odoo/addons/payment/views/payment_views.xml
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
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
