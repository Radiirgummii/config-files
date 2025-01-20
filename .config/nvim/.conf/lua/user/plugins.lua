-- Plugins

local lazy = {}

function lazy.install(path)
  if not vim.loop.fs_stat(path) then
    print('Installing lazy.nvim....')
    vim.fn.system({
      'git',
      'clone',
      '--filter=blob:none',
      'https://github.com/folke/lazy.nvim.git',
      '--branch=stable', -- latest stable release
      path,
    })
  end
end

function lazy.setup(plugins)
  if vim.g.plugins_ready then
    return
  end



  vim.opt.rtp:prepend(lazy.path)

  require('lazy').setup(plugins, lazy.opts)
  vim.g.plugins_ready = true
end


lazy.path = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'

lazy.opts = {}

lazy.setup({
  {'folke/tokyonight.nvim'},
  {'nvim-lualine/lualine.nvim'},
  {'neovim/nvim-lspconfig'},
  {'hrsh7th/nvim-cmp'},
  {'hrsh7th/cmp-nvim-lsp'},
  {
    "iamcco/markdown-preview.nvim",
    cmd = { "MarkdownPreviewToggle", "MarkdownPreview", "MarkdownPreviewStop" },
    build = "cd app && yarn install",
    init = function()
      vim.g.mkdp_filetypes = { "markdown" }
    end,
    ft = { "markdown" }
  },
})


vim.opt.termguicolors = true
vim.cmd.colorscheme('tokyonight')
require('lualine').setup({
  options = {
    icons_enabled = false,
  }
})
vim.g.netrw_banner = 0
vim.g.netrw_winsize = 30
vim.keymap.set('n', 'E', '<cmd>Lexplore<cr>')

