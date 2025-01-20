vim.opt.number = true
vim.opt.mouse = 'a'
vim.opt.smartcase = true
vim.opt.wrap = true
vim.opt.breakindent = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.keymap.set({'n', 'x'}, 'C', '"+y')
vim.keymap.set({'n', 'x'}, 'P', '"+p')


--Plugins
require("user/plugins")

--LSP
require("user/lsp")

require("user/markdown_preview")
